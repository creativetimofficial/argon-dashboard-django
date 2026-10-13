import numpy as np
import matplotlib.pyplot as plt

def set_default_cell_styles(kwargs):
  if not (('c' in kwargs) or ('color' in kwargs)):
    kwargs['c'] = 'gray'
  if not ('alpha' in kwargs):
    kwargs['alpha'] = 0.6
  if not (('lw' in kwargs) or ('linewidth' in kwargs)):
    kwargs['lw'] = 2

def draw_cell(ax, axes, corner=None, enclose=True, **kwargs):
  ndim = len(axes)
  if ndim not in [2, 3]:
    raise RuntimeError('ndim = %d is not supported' % ndim)
  cell = []
  if corner is None:
    corner = np.zeros(ndim)

  set_default_cell_styles(kwargs)

  # a,b,c lattice vectors
  for iax in range(ndim):
    start = corner
    end   = start + axes[iax]
    line = ax.plot(*zip(start, end), **kwargs)
    cell.append(line)

  if enclose:
    # counter a,b,c vectors
    for iax in range(ndim):
      start = corner+axes.sum(axis=0)
      end   = start - axes[iax]
      line = ax.plot(*zip(start, end), **kwargs)
      cell.append(line)

    if ndim > 2:
      # remaining vectors needed to enclose cell
      for iax in range(ndim):
        start = corner+axes[iax]
        for jax in range(ndim):
          if jax == iax:
            continue
          end = start + axes[jax]
          line = ax.plot(*zip(start, end), **kwargs)
          cell.append(line)
  # end if enclose
  return cell

ndim = 2

# square
cell = np.eye(ndim)
pos = np.zeros([1, ndim])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect=1)
draw_cell(ax, cell)
ax.plot(*pos.T, ls='', marker='.')
fig.savefig('square.png', dpi=320)

# honeycomb
cell = np.array([
    [1, 0],
    [-0.5, 3**0.5/2],
])
fracs = np.array([
    [0, 0],
    [1./3, 2./3],
])
pos = fracs @ cell

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect=1)
draw_cell(ax, cell)
ax.plot(*pos.T, ls='', marker='.')

plt.show()