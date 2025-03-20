import itertools
import sys

import minineedle
import miniseq as ms

from minineedle.needle import NeedlemanWunsch
from minineedle.core import ScoreMatrix

ch_offset = 96


def transform_line_order_to_sequence(line_numbers):
    sequence = ''
    for number in line_numbers:
        if number <= 0 or number >= 27:
            print('Ignore match in line ' + str(number) + ' as it breaks the algorithm.')
            continue
        letter = chr(number + ch_offset)
        sequence += letter

    return sequence

def nwalign_and_compute_nw_score_naive(line_numbers_model, line_numbers_gaze):
    if not line_numbers_model:
        return 0

    model = transform_line_order_to_sequence(line_numbers_model)
    gaze = transform_line_order_to_sequence(line_numbers_gaze)

    seq_model = ms.Sequence('Model', model)
    seq_gaze = ms.Sequence('Actual', gaze)

    alignment = NeedlemanWunsch(seq_model, seq_gaze)
    alignment.change_matrix(ScoreMatrix(match=3, miss=-3, gap=-2))

    try:
        alignment.align()

        score = alignment.get_score()

    except ZeroDivisionError as e:
        print('ZeroDivisionError when comparing the following numbers')
        print('repeated ', line_numbers_model)
        print('gaze     ', line_numbers_gaze)

        score = 0

    return score

def nwalign_and_compute_nw_score_dynamic(line_numbers_model, line_numbers_gaze):
    if not line_numbers_model:
        return [0, 0]

    length_gaze = len(line_numbers_gaze)

    high_score = None
    repetitions = None

    multiplicator = 1

    while True:
        model = list(itertools.chain.from_iterable(itertools.repeat(line_numbers_model, multiplicator)))
        length_model = len(model)

        score = nwalign_and_compute_nw_score_naive(model, line_numbers_gaze)

        if not high_score or score > high_score:
            high_score = score
            repetitions = multiplicator

        multiplicator += 1

        if length_model > length_gaze:
            break

    return [repetitions, high_score]

#### Note that this implementation of NW Algorithm is directly taken from previous work by Apel. 
#### The implementation is slightly adjusted to fit our work. 