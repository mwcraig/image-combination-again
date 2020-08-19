# Everything below allows for masking

def combine_chunking_machinery(zero_offset=None,
                   scaling=None, # computing value from the data
                                 # to modify by (or a number)
                   mem_limit=1e8, dtype=None):
    pass

def combine_arrays(arrays,
                   output_file=None,
                   method='average' or 'median' or 'sum',
                   weights=None,
                   clipping_method='minmax' or 'sigma' or 'none' or 'extrema',
                   clip_limits=(lo, hi),
                   variance=None):
                   # clipping methods
                   # clip_extrema=False, nlow=1, nhigh=1,
                   # minmax_clip=False, minmax_clip_min=None, minmax_clip_max=None,
                   # sigma_clip=False,
                   # sigma_clip_low_thresh=3, sigma_clip_high_thresh=3,
                   # sigma_clip_func=ma.mean, sigma_clip_dev_func=ma.std,

    """
    Returns
    -------

    combined image
    combined variance array (if variance provided) or estimated (if none provided)
    mask - True where masked
    """

    pass

def median()

def median_absolute_deviation()

def sigma_clipping()
