#
import data_serialize
import numpy as np


def test_feature():
    val1 = data_serialize.Int64List(value=[1, 2, 3] * 20)
    val2 = data_serialize.FloatList(value=[1, 2, 3] * 20)
    val3 = data_serialize.BytesList(value=[b'The china', b'boy'])

    featrue = data_serialize.Features(feature=
    {
        "item_0": data_serialize.Feature(int64_list=val1),
        "item_1": data_serialize.Feature(float_list=val2),
        "item_2": data_serialize.Feature(bytes_list=val3)
    }
    )

    example = data_serialize.Example(features=featrue)

    # 序列化
    serialize = example.SerializeToString()
    print(serialize)

    # 反序列化
    example = data_serialize.Example()
    example.ParseFromString(serialize)
    print(example)


def test_numpyobject():
    a = np.random.randint(0, 21128, size=(10,), dtype=np.int64)
    b = np.random.rand(3, 4)
    c = np.asarray(b'111111111aaaaaaaaaa')

    val1 = data_serialize.NumpyObject(
        header='',
        dtype=str(a.dtype),
        shape=list(a.shape),
        int64=a.reshape((-1,)).tolist(),
    )
    val2 = data_serialize.NumpyObject(
        header='',
        dtype=str(b.dtype),
        shape=list(b.shape),
        float64=b.reshape((-1,)).tolist(),
    )
    val3 = data_serialize.NumpyObject(
        header='',
        dtype=str(c.dtype),
        shape=list(c.shape),
        bytes=c.tobytes(),
    )

    example = data_serialize.NumpyObjectMap(numpyobjects={
        "item_0": val1,
        "item_1": val2,
        "item_2": val3}
    )
    # 序列化
    serialize = example.SerializeToString()
    print(serialize)

    # 反序列化
    example = data_serialize.NumpyObjectMap()
    example.ParseFromString(serialize)
    print(example)


test_feature()

test_numpyobject()
