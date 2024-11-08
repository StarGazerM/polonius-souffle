# polonius-souffle
souffle version of polonius

# dataset
There is a extracted dataset from `clap-rs` under `polonius/input` folder, original dataset is using string.
If your engine don't support string, use script `fact_encode.py` to generated a number version.

# analysis
All analysis datalog code are in `polonius.dl`. It is a datalog version rust borrow-checker. It include a
liveness analysis, which is very classic.

