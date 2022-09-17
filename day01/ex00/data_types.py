def data_types() -> None:
    a = 1
    b = "hi"
    c = 1.0
    d = False
    e = []
    f = {}
    g = ()
    h = set()
    print('[%s, %s, %s, %s, %s, %s, %s, %s]'
          % (
              type(a).__name__, type(b).__name__,
              type(c).__name__, type(d).__name__,
              type(e).__name__, type(f).__name__,
              type(g).__name__, type(h).__name__
          )
          )

if __name__ == '__main__':
    data_types()