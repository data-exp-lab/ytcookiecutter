{%- if cookiecutter.frontend_type|lower == "stream: uniform grid" %}
from yt.loaders import load_uniform_grid

def load(filename: str):

    # write code to load data from filename into memory!

    data = ????????
    domain_dimensions = ????????

    # set or delete optional kwargs
    length_unit = None
    bbox = None
    nprocs = 1
    sim_time = 0.0
    mass_unit = None
    time_unit = None
    velocity_unit = None
    magnetic_unit = None
    periodicity = (True, True, True)
    geometry = 'cartesian'
    unit_system = 'cgs'
    default_species_fields = None

    # call the stream data loader.
    ds = load_uniform_grid(
        data,
        domain_dimensions,
        length_unit=length_unit,
        bbox=bbox,
        nprocs=nprocs,
        sim_time=sim_time,
        mass_unit=mass_unit,
        time_unit=time_unit,
        velocity_unit=velocity_unit,
        magnetic_unit=magnetic_unit,
        periodicity=periodicity,
        geometry=geometry,
        unit_system=unit_system,
        default_species_fields=default_species_fields,
        )


    # return the in-memory ds
    return ds

# description of load_uniform_grid for convenience:
{%- endif %}

{%- if cookiecutter.frontend_type|lower == "stream: amr grids" %}
from yt.loaders import load_amr_grids

def load(filename: str):

    # write code to load data from filename into memory!

    grid_data = ????????
    domain_dimensions = ????????

    # set or delete optional kwargs
    bbox = None
    sim_time = 0.0
    length_unit = None
    mass_unit = None
    time_unit = None
    velocity_unit = None
    magnetic_unit = None
    periodicity = (True, True, True)
    geometry = 'cartesian'
    refine_by = 2
    unit_system = 'cgs'
    default_species_fields = None

    # call the stream data loader.
    ds = load_amr_grids(
        grid_data,
        domain_dimensions,
        bbox=bbox,
        sim_time=sim_time,
        length_unit=length_unit,
        mass_unit=mass_unit,
        time_unit=time_unit,
        velocity_unit=velocity_unit,
        magnetic_unit=magnetic_unit,
        periodicity=periodicity,
        geometry=geometry,
        refine_by=refine_by,
        unit_system=unit_system,
        default_species_fields=default_species_fields,
        )


    # return the in-memory ds
    return ds

# description of load_amr_grids for convenience:
{%- endif %}

{%- if cookiecutter.frontend_type|lower == "stream: particles" %}
from yt.loaders import load_particles

def load(filename: str):

    # write code to load data from filename into memory!

    data = ????????

    # set or delete optional kwargs
    length_unit = None
    bbox = None
    sim_time = None
    mass_unit = None
    time_unit = None
    velocity_unit = None
    magnetic_unit = None
    periodicity = (True, True, True)
    geometry = 'cartesian'
    unit_system = 'cgs'
    data_source = None
    default_species_fields = None

    # call the stream data loader.
    ds = load_particles(
        data,
        length_unit=length_unit,
        bbox=bbox,
        sim_time=sim_time,
        mass_unit=mass_unit,
        time_unit=time_unit,
        velocity_unit=velocity_unit,
        magnetic_unit=magnetic_unit,
        periodicity=periodicity,
        geometry=geometry,
        unit_system=unit_system,
        data_source=data_source,
        default_species_fields=default_species_fields,
        )


    # return the in-memory ds
    return ds

# description of load_particles for convenience:
{%- endif %}

{%- if cookiecutter.frontend_type|lower == "stream: octree" %}
from yt.loaders import load_octree

def load(filename: str):

    # write code to load data from filename into memory!

    octree_mask = ????????
    data = ????????

    # set or delete optional kwargs
    bbox = None
    sim_time = 0.0
    length_unit = None
    mass_unit = None
    time_unit = None
    velocity_unit = None
    magnetic_unit = None
    periodicity = (True, True, True)
    over_refine_factor = 1
    partial_coverage = 1
    unit_system = 'cgs'
    default_species_fields = None

    # call the stream data loader.
    ds = load_octree(
        octree_mask,
        data,
        bbox=bbox,
        sim_time=sim_time,
        length_unit=length_unit,
        mass_unit=mass_unit,
        time_unit=time_unit,
        velocity_unit=velocity_unit,
        magnetic_unit=magnetic_unit,
        periodicity=periodicity,
        over_refine_factor=over_refine_factor,
        partial_coverage=partial_coverage,
        unit_system=unit_system,
        default_species_fields=default_species_fields,
        )


    # return the in-memory ds
    return ds

# description of load_octree for convenience:
{%- endif %}

{%- if cookiecutter.frontend_type|lower == "stream: hexahedral mesh" %}
from yt.loaders import load_hexahedral_mesh

def load(filename: str):

    # write code to load data from filename into memory!

    data = ????????
    connectivity = ????????
    coordinates = ????????

    # set or delete optional kwargs
    length_unit = None
    bbox = None
    sim_time = 0.0
    mass_unit = None
    time_unit = None
    velocity_unit = None
    magnetic_unit = None
    periodicity = (True, True, True)
    geometry = 'cartesian'
    unit_system = 'cgs'

    # call the stream data loader.
    ds = load_hexahedral_mesh(
        data,
        connectivity,
        coordinates,
        length_unit=length_unit,
        bbox=bbox,
        sim_time=sim_time,
        mass_unit=mass_unit,
        time_unit=time_unit,
        velocity_unit=velocity_unit,
        magnetic_unit=magnetic_unit,
        periodicity=periodicity,
        geometry=geometry,
        unit_system=unit_system,
        )


    # return the in-memory ds
    return ds

# description of load_hexahedral_mesh for convenience:
{%- endif %}

{%- if cookiecutter.frontend_type|lower == "stream: unstructured mesh" %}
from yt.loaders import load_unstructured_mesh

def load(filename: str):

    # write code to load data from filename into memory!

    connectivity = ????????
    coordinates = ????????

    # set or delete optional kwargs
    node_data = None
    elem_data = None
    length_unit = None
    bbox = None
    sim_time = 0.0
    mass_unit = None
    time_unit = None
    velocity_unit = None
    magnetic_unit = None
    periodicity = (False, False, False)
    geometry = 'cartesian'
    unit_system = 'cgs'

    # call the stream data loader.
    ds = load_unstructured_mesh(
        connectivity,
        coordinates,
        node_data=node_data,
        elem_data=elem_data,
        length_unit=length_unit,
        bbox=bbox,
        sim_time=sim_time,
        mass_unit=mass_unit,
        time_unit=time_unit,
        velocity_unit=velocity_unit,
        magnetic_unit=magnetic_unit,
        periodicity=periodicity,
        geometry=geometry,
        unit_system=unit_system,
        )


    # return the in-memory ds
    return ds

# description of load_unstructured_mesh for convenience:
{%- endif %}

