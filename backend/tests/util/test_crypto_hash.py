from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # testing to check if it creates the same hash with arguments data types in any order
    assert crypto_hash(1,[2],'three') ==  crypto_hash('three',1,[2])
    assert crypto_hash('foo') == 'asdf'