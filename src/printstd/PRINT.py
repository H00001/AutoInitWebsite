import sys
class PRINT_STD :
    isSil = False
    @classmethod
    def P(cls, param):
        if not cls.isSil:
            sys.stdout.write(param)
        else:
            pass

    @classmethod
    def E(cls, param):
        if not cls.isSil:
            sys.stderr.write(param)
        else:
            pass
