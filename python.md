# python

# cProfile

```python
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
# insert function executing
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CUMULATIVE)
ps.print_stats(10)
print(s.getvalue())
```
