from client import SeqLock

def main():
    print("=== Testing Sequential Lock (SeqLock) ===")
    sl = SeqLock()
    sl.write("active_users", 1500)

    res = sl.read("active_users")
    print("SeqLock read result:", res)
    assert res['val'] == 1500
    assert res['consistent'] is True

    print("Sequential Lock verified successfully!")

if __name__ == '__main__':
    main()
