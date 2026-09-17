import numpy as np

def manual_train_test_split(X, y_int, y_onehot, *, test_fraction=0.2, seed=0):
    """
    Split manually into train/test subsets.
    Returns:
        X_train, y_train_int, y_train_onehot,
        X_test,  y_test_int,  y_test_onehot
    """
    rng = np.random.default_rng(seed)
    N = X.shape[0]
    indices = rng.permutation(N)
    test_size = int(N * test_fraction)
    test_idx = indices[:test_size]
    train_idx = indices[test_size:]

    return (X[train_idx], y_int[train_idx], y_onehot[train_idx],
            X[test_idx],  y_int[test_idx],  y_onehot[test_idx])
def relu(x):
    return np.maximum(0.0, x)

def relu_grad(x):
    return (x > 0).astype(float)

def softmax(logits):
    logits = logits - logits.max(axis=1, keepdims=True)
    ex = np.exp(logits)
    return ex / ex.sum(axis=1, keepdims=True)

def build(input_dim, hidden_layers, output_dim,
              activation='relu',
              use_dropout=False,
              dropout_rate=0.2,
              batch_size=32,
              learning_rate=1e-3,
              seed=None):

    rng = np.random.default_rng(seed)
    params = {}
    feature_dim = input_dim

    # dense layers
    for i, width in enumerate(hidden_layers):
        params[f'W{i}'] = rng.normal(scale=np.sqrt(2.0 / feature_dim), size=(feature_dim, width))
        params[f'b{i}'] = np.zeros(width)
        feature_dim = width

    # output layer
    params['W_out'] = rng.normal(scale=np.sqrt(2.0 / feature_dim), size=(feature_dim, output_dim))
    params['b_out'] = np.zeros(output_dim)

    config = dict(
        input_dim=input_dim,
        output_dim=output_dim,
        hidden_layers=list(hidden_layers),
        activation=activation,
        use_dropout=use_dropout,
        dropout_rate=dropout_rate,
        batch_size=batch_size,
        learning_rate=learning_rate,
        seed=seed
    )

    return config, params

def forward(x, params, config, *, train=False, rng=None):
    cache = dict(inputs=[], preacts=[], drop_masks=[])
    out = x

    keep_prob = 1 - config['dropout_rate']

    for i, width in enumerate(config['hidden_layers']):
        cache['inputs'].append(out)
        z = out @ params[f'W{i}'] + params[f'b{i}']
        cache['preacts'].append(z)

        out = relu(z)

        # dropout
        if config['use_dropout'] and train:
            if rng is None:
                rng = np.random.default_rng()
            mask = (rng.random(out.shape) < keep_prob).astype(float) / keep_prob
            out *= mask
            cache['drop_masks'].append(mask)
        else:
            cache['drop_masks'].append(None)

    cache['final_hidden'] = out
    logits = out @ params['W_out'] + params['b_out']
    return logits, cache

def backward(probs, targets, cache, params, config):
    grads = {}
    B = targets.shape[0]

    # dL/dlogits
    dlogits = (probs - targets) / B

    # output layer grads
    H = cache['final_hidden']
    grads['W_out'] = H.T @ dlogits
    grads['b_out'] = dlogits.sum(axis=0)

    dprev = dlogits @ params['W_out'].T

    # hidden layers backward
    for i in reversed(range(len(config['hidden_layers']))):
        # dropout
        if cache['drop_masks'][i] is not None:
            dprev *= cache['drop_masks'][i]

        # relu grad
        dz = relu_grad(cache['preacts'][i]) * dprev

        X_prev = cache['inputs'][i]
        grads[f'W{i}'] = X_prev.T @ dz
        grads[f'b{i}'] = dz.sum(axis=0)

        dprev = dz @ params[f'W{i}'].T

    return grads

def train(X_train, y_train, X_test, y_test, config, params, epochs=15):
    rng = np.random.default_rng(config['seed'])
    bs = config['batch_size']
    lr = config['learning_rate']

    train_losses = []
    test_accs = []

    for epoch in range(epochs):

        # shuffle
        idx = rng.permutation(len(X_train))
        Xs = X_train[idx]
        ys = y_train[idx]

        total_loss = 0
        num_batches = int(np.ceil(len(X_train)/bs))

        for b in range(num_batches):
            start = b*bs
            end   = start+bs
            Xb = Xs[start:end]
            yb = ys[start:end]

            logits, cache = forward(Xb, params, config, train=True, rng=rng)
            probs = softmax(logits)
            loss = -np.sum(yb * np.log(probs+1e-8)) / len(Xb)
            total_loss += loss

            grads = backward(probs, yb, cache, params, config)

            # update
            for k in grads:
                params[k] -= lr * grads[k]

        avg_loss = total_loss / num_batches
        train_losses.append(avg_loss)

        # ---- evaluate ----
        logits_test, _ = forward(X_test, params, config, train=False)
        probs_test = softmax(logits_test)
        preds = np.argmax(probs_test, axis=1)
        truth = np.argmax(y_test, axis=1)
        acc = (preds == truth).mean() * 100
        test_accs.append(acc)

        print(f"Epoch {epoch+1}/{epochs} | Loss {avg_loss:.4f} | Test Acc: {acc:.2f}%")

    return params, train_losses, test_accs

