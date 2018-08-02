"""My (Akeley's) attempt at writing a test for a 1D bit line buffer."""

from itertools import chain
from magma.simulator.coreir_simulator import CoreIRSimulator
import coreir
from magma.scope import Scope

def test_1D_bit_line_buffer():
    """Run tests for the 1D bit line buffer."""
    
    # Need these 2 for some reason.
    c = coreir.Context()
    scope = Scope()

    

def expected_valid_outputs(pixels_per_clock: int,
                           window_width: int,
                           image_size: int,
                           output_stride: int,
                           origin: int,
                           in_arrays):
    """Given 1D bit line buffer parameters and a list of lists of pixel
    values representing the stream of input (one entry = one clock
    cycles' array-of-pixels input), return a list-of-lists-of-lists of
    values (None for garbage) representing outputs on cycles where the
    linebuffer asserts valid, in the order:
        outer dim:   time
        middle dim:  list of windows (parallelism)
        inner dim:   pixels within a window
    """
    stride = output_stride
    if len(in_arrays) * pixels_per_clock != image_size:
        raise Exception(
            "Expected in_arrays length of %g"
                 % (image_size/pixels_per_clock)
            + f" for pixels_per_clock {pixels_per_clock}"
            + f" and image_size {image_size}."
        )

    # index -> pixel
    pixel_dict = {i:b for i,b in enumerate(chain(*in_arrays))}

    # Total number of windows outputted.
    window_count = image_size//stride
    
    # Number of parallel window outputs.
    parallelism = pixels_per_clock//stride
    if parallelism == 0:
        parallelism = 1
    else:
        assert parallelism*stride == pixels_per_clock, \
            "Expected integer throughput (stride evenly dividing px/clk)."
    
    # Number of times valid should be asserted.
    valid_count = window_count//parallelism
    assert valid_count * parallelism == window_count, \
        "Expected window count (img/stride) to be divisible by parallelism " \
        "(px/clk / stride)"

    return [
        [
            [
                pixel_dict.get(window_offset + pixel_offset)
                for pixel_offset in range(window_width)
            ]
            for window_offset # index of left pixel of window.
            in range(origin + parallelism * stride * time_idx,
                     origin + parallelism * stride * (1+time_idx),
                     stride)
        ]
        for time_idx in range(valid_count)
    ]


