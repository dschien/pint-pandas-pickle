
import pandas as pd
import pint

def run():
    df = pd.DataFrame({
        "torque": pd.Series([1, 2, 2, 3], dtype="pint[lbf ft]"),
        "angular_velocity": pd.Series([1, 2, 2, 3], dtype="pint[rpm]"),
    })
    store = pd.HDFStore('test.hdf5')

    metadata = {}
    for process, variable in df.items():
        metadata[process] = variable.pint.units

    store.put('model_data', df.pint.dequantify())
    store.get_storer('model_data').attrs.metadata = metadata

    store.close()


if __name__ == '__main__':
    run()
