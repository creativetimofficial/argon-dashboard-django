# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Sample data for contributors - in a real app, this would come from a database
CONTRIBUTORS = {
    'paul-yang': {
        'name': 'Dr. Paul Yang',
        'role': 'Principal Investigator',
        'department': 'Department of Physics',
        'image': '/static/assets/img/theme/paul.jpg',
        'bio': 'Dr. Yang is a distinguished researcher in materials science and quantum computing. His work focuses on developing new computational methods for studying quantum systems and their applications in materials discovery.',
        'publications': 3,
        'citations': 8,
        'projects': 5,
        'email': 'Paul.Yang@hofstra.edu',
        # 'phone': '+1 (555) 123-4567',
        'Website': 'https://paul-st-young.github.io/cv/',
        'interests': ['Quantum Computing', 'Materials Science', 'Computational Physics'],
       
        'current_work': [
            # 'Developing quantum algorithms for materials discovery',
            # 'Building open-source quantum simulation frameworks',
            # 'Collaborating on quantum machine learning applications'
        ]
    },
    'emilia-szynwald': {
        'name': 'Emilia Szynwald',
        'role': 'Undergraduate Research Student',
        'department': 'Department of Computer Science',
        'image': '/static/assets/img/theme/emilia.png',
        'bio': 'Emilia specializes in Computer Science and machine learning. Her research combines cutting-edge ML techniques with traditional computational physics methods to predict molecular properties and accelerate elemental physics discorveries.',
      
        'email': 'ESzynwald1@pride.hofstra.edu',
     

        'interests': ['Computational Physics', 'Machine Learning', 'Quantum Physics'],
        'recent_publications': [
            
        ],
        'current_work': [
            'Modeling Charged Multilayer Devices with Defects Using JAX',
        ]
    },
    'cameron getner': {
        'name': 'Cameron Getner',
        'role': 'Undergraduate Research Student',

        'image': '/static/assets/img/theme/cameron.png',
        'bio': 'Cameron is a talented undergraduate researcher specializing in computational physics and scientific visualization. Her work focuses on creating interactive tools and simulations that make complex physics concepts more accessible to students and researchers.',
        # 'publications': 0,
        # 'citations': 0,
        # 'projects': 1,
        'email': 'MBogartGetner1@pride.hofstra.edu',
        # 'phone': 'placeholder',
        # 'office': 'Physics Building, Room 412',
        'interests': ['Computational Physics', ],
        'recent_publications': [
          
        ],
        'current_work': [
            
            'Using DFT to simulate electrons in moiré superlattices'
        ]
    }
}

from .cell_visualization import get_cell_plots


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def cells(request):
    """
    added: Added form handling for custom cell visualization
    - Accepts POST data: cell_type, lattice_constant, marker_size, line_width
    - Generates visualization only on form submission (POST)
    - Returns only selected cell type (square or honeycomb)
    """
    # Default values
    cell_type = 'square'
    lattice_constant = 1.0
    marker_size = 10
    line_width = 2
    cell_image = None
    
    # Handle form submission
    if request.method == 'POST':
        cell_type = request.POST.get('cell_type', 'square')
        try:
            lattice_constant = float(request.POST.get('lattice_constant', 1.0))
            marker_size = int(request.POST.get('marker_size', 10))
            line_width = float(request.POST.get('line_width', 2))
        except (ValueError, TypeError):
            # If conversion fails, use defaults
            pass
        
        # Generate only the selected cell type
        from .cell_visualization import generate_single_cell
        cell_image = generate_single_cell(cell_type, lattice_constant, marker_size, line_width)
    
    context = {
        'segment': 'cells',
        'cell_image': cell_image,
        'cell_type': cell_type,
        'lattice_constant': lattice_constant,
        'marker_size': marker_size,
        'line_width': line_width,
    }
    html_template = loader.get_template('home/cells.html')
    return HttpResponse(html_template.render(context, request))

def cameron_research(request):
    """
    Cameron Getner's research page on DFT simulations of moiré superlattices
    """
    context = {
        'segment': 'cameron_research'
    }
    html_template = loader.get_template('home/cameron_research.html')
    return HttpResponse(html_template.render(context, request))

def people(request):
    context = {
        'contributors': CONTRIBUTORS,
        'segment': 'people'
    }
    html_template = loader.get_template('home/people.html')
    return HttpResponse(html_template.render(context, request))

def profile(request, username):
    if username not in CONTRIBUTORS:
        return HttpResponseRedirect('/page-404.html')
    
    context = {
        'person': CONTRIBUTORS[username],
        'segment': 'people'
    }
    html_template = loader.get_template('home/profile.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
