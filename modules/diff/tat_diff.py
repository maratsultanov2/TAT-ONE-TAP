class TATDiff:
    def compute(self, old, new):
        return 't:+0.01,r:-0.02,e:+0.07,m:-0.01,g:0.00'

    def apply(self, state, diff):
        return state
