"""
added: Added customizable cell visualization
- get_cell_plots(): Updated to accept lattice_constant, marker_size, line_width parameters
- generate_single_cell(): NEW function - generates only one cell type (square or honeycomb) based on user selection
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Set the backend before importing pyplot
import matplotlib.pyplot as plt
import io
import base64

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
    return cell

def get_cell_plots(lattice_constant=1.0, marker_size=10, line_width=2):
    plots = []
    ndim = 2

    # square cell
    plt.close('all')
    fig = plt.figure(figsize=(8, 8), dpi=100)
    ax = fig.add_subplot(1, 1, 1, aspect='equal')
    
    cell = np.eye(ndim) * lattice_constant
    pos = np.zeros([1, ndim])
    draw_cell(ax, cell, lw=line_width)
    ax.plot(*pos.T, ls='', marker='o', markersize=marker_size, color='blue')
    ax.set_title('Square Cell', fontsize=14, pad=20)
    ax.grid(True, linestyle='--', alpha=0.3)
    margin = 0.2 * lattice_constant
    ax.set_xlim(-margin, lattice_constant + margin)
    ax.set_ylim(-margin, lattice_constant + margin)
    
    # Convert plot to PNG
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', facecolor='white', edgecolor='none')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    plots.append(graphic.decode('utf-8'))

    # honeycomb cell
    plt.close('all')
    fig = plt.figure(figsize=(8, 8), dpi=100)
    ax = fig.add_subplot(1, 1, 1, aspect='equal')
    
    cell = np.array([
        [1, 0],
        [-0.5, 3**0.5/2],
    ]) * lattice_constant
    fracs = np.array([
        [0, 0],
        [1./3, 2./3],
    ])
    pos = fracs @ cell
    draw_cell(ax, cell, lw=line_width)
    ax.plot(*pos.T, ls='', marker='o', markersize=marker_size, color='blue')
    ax.set_title('Honeycomb Cell', fontsize=14, pad=20)
    ax.grid(True, linestyle='--', alpha=0.3)
    margin = 0.2 * lattice_constant
    ax.set_xlim(-0.7 * lattice_constant, 1.2 * lattice_constant)
    ax.set_ylim(-margin, 1.2 * lattice_constant)
    
    # Convert plot to PNG
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', facecolor='white', edgecolor='none')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    plots.append(graphic.decode('utf-8'))
    
    plt.close('all')
    return plots

def generate_single_cell(cell_type, lattice_constant=1.0, marker_size=10, line_width=2):
    """
    Generate a single cell visualization based on cell type.
    
    Args:
        cell_type: 'square' or 'honeycomb'
        lattice_constant: Size of the unit cell
        marker_size: Size of atoms/points
        line_width: Width of cell edges
    
    Returns:
        Base64 encoded PNG image
    """
    ndim = 2
    plt.close('all')
    fig = plt.figure(figsize=(8, 8), dpi=100)
    ax = fig.add_subplot(1, 1, 1, aspect='equal')
    
    if cell_type == 'square':
        cell = np.eye(ndim) * lattice_constant
        pos = np.zeros([1, ndim])
        draw_cell(ax, cell, lw=line_width)
        ax.plot(*pos.T, ls='', marker='o', markersize=marker_size, color='blue')
        ax.set_title('Square Cell', fontsize=14, pad=20)
        ax.grid(True, linestyle='--', alpha=0.3)
        margin = 0.2 * lattice_constant
        ax.set_xlim(-margin, lattice_constant + margin)
        ax.set_ylim(-margin, lattice_constant + margin)
    else:  # honeycomb
        cell = np.array([
            [1, 0],
            [-0.5, 3**0.5/2],
        ]) * lattice_constant
        fracs = np.array([
            [0, 0],
            [1./3, 2./3],
        ])
        pos = fracs @ cell
        draw_cell(ax, cell, lw=line_width)
        ax.plot(*pos.T, ls='', marker='o', markersize=marker_size, color='blue')
        ax.set_title('Honeycomb Cell', fontsize=14, pad=20)
        ax.grid(True, linestyle='--', alpha=0.3)
        margin = 0.2 * lattice_constant
        ax.set_xlim(-0.7 * lattice_constant, 1.2 * lattice_constant)
        ax.set_ylim(-margin, 1.2 * lattice_constant)
    
    # Convert plot to PNG
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight', facecolor='white', edgecolor='none')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    plt.close('all')
    
    return graphic.decode('utf-8')