#!/usr/bin/env python3

import collections
import graderUtil
import random

grader = graderUtil.Grader()

try:
    import solution
    SEED = solution.SEED
    solution_exists = True
except ModuleNotFoundError:
    SEED = 42
    solution_exists = False

submission = grader.load('submission')
grader.useSolution = solution_exists

############################################################
# check python version

import sys
import warnings

if not (sys.version_info[0] == 3 and sys.version_info[1] == 12):
    warnings.warn("Must be using Python 3.12 \n")


############################################################
# Problem 5a: find_longest_lexicographically_first_word

grader.add_basic_part(
    '5a-0-basic',
    lambda: grader.require_is_equal(
        'alphabetically',
        submission.find_longest_lexicographically_first_word('which is the first word alphabetically')
    ),
    max_points=1,
    description='longest word; tie-break lexicographically'
)

grader.add_basic_part(
    '5a-1-basic',
    lambda: grader.require_is_equal(
        'bbb',
        submission.find_longest_lexicographically_first_word('bbb a cc ddd')
    ),
    max_points=1,
    description='simple test case'
)

grader.add_basic_part(
    '5a-2-basic',
    lambda: grader.require_is_equal(
        '10000',
        submission.find_longest_lexicographically_first_word(' '.join(str(x) for x in range(100000)))
    ),
    max_points=2,
    description='big test case'
)

############################################################
# Problem 5b: manhattan_distance

grader.add_basic_part(
    '5b-0-basic',
    lambda: grader.require_is_equal(7, submission.manhattan_distance((1, 5), (4, 1))),
    max_points=1,
    description='simple test case'
)


def test5b1():
    random.seed(42)
    for _ in range(100):
        x1 = random.randint(0, 10)
        y1 = random.randint(0, 10)
        x2 = random.randint(0, 10)
        y2 = random.randint(0, 10)
        ans2 = submission.manhattan_distance((x1, y1), (x2, y2))
        if solution_exists:
            grader.require_is_equal(ans2, solution.manhattan_distance((x1, y1), (x2, y2)))

grader.add_hidden_part('5b-1-hidden', test5b1, max_points=2, description='100 random trials')


############################################################
# Problem 5c: mutate_sentences (start/end fixed)
def _validate_mutations(original: str, outputs):
    words = original.split()
    L = len(words)

    if not isinstance(outputs, list):
        grader.fail("Expected a list of strings.")
        return
    for s in outputs:
        if not isinstance(s, str):
            grader.fail("Expected a list of strings.")
            return

    # No duplicates
    grader.require_is_equal(len(outputs), len(set(outputs)))

    if L == 0:
        grader.require_is_equal([], outputs)
        return

    start_word = words[0]
    end_word = words[-1]

    # Build allowed bigrams from original
    allowed = set()
    for i in range(L - 1):
        allowed.add((words[i], words[i + 1]))

    for sent in outputs:
        toks = sent.split()
        grader.require_is_equal(L, len(toks))
        grader.require_is_equal(start_word, toks[0])
        grader.require_is_equal(end_word, toks[-1])
        for i in range(L - 1):
            grader.require_is_true((toks[i], toks[i + 1]) in allowed)


def test5c0():
    out = submission.mutate_sentences('a a a a a')
    grader.require_is_equal(sorted(['a a a a a']), sorted(out))
    _validate_mutations('a a a a a', out)

    out = submission.mutate_sentences('the cat')
    grader.require_is_equal(sorted(['the cat']), sorted(out))
    _validate_mutations('the cat', out)

    out = submission.mutate_sentences('the cat and the mouse')
    grader.require_is_equal(sorted(['the cat and the mouse']), sorted(out))
    _validate_mutations('the cat and the mouse', out)

    out = submission.mutate_sentences('the red the blue the end')
    grader.require_is_equal(
        sorted([
            'the red the blue the end',
            'the blue the red the end',
            'the red the red the end',
            'the blue the blue the end',
        ]),
        sorted(out),
    )
    _validate_mutations('the red the blue the end', out)


grader.add_basic_part('5c-0-basic', test5c0, max_points=1, description='simple tests')


def gen_sentence(alphabet_size, length):
    return ' '.join(str(random.randint(0, alphabet_size)) for _ in range(length))


def test5c1():
    random.seed(SEED)
    for _ in range(10):
        sentence = gen_sentence(3, 5)
        ans2 = submission.mutate_sentences(sentence)
        if solution_exists:
            grader.require_is_equal(sorted(ans2), sorted(solution.mutate_sentences(sentence)))

grader.add_hidden_part('5c-1-hidden', test5c1, max_points=2, description='random trials')


def test5c2():
    random.seed(SEED)
    for _ in range(10):
        sentence = gen_sentence(25, 10)
        ans2 = submission.mutate_sentences(sentence)
        if solution_exists:
            grader.require_is_equal(sorted(ans2), sorted(solution.mutate_sentences(sentence)))

grader.add_hidden_part('5c-2-hidden', test5c2, max_points=3, description='random trials (bigger)')


############################################################
# Problem 5d: sparse_vector_dot_product
def test5d0():
    grader.require_is_equal(
        15,
        submission.sparse_vector_dot_product(
            collections.defaultdict(float, {'a': 5}),
            collections.defaultdict(float, {'b': 2, 'a': 3})
        )
    )


grader.add_basic_part('5d-0-basic', test5d0, max_points=1, description='simple test')


def randvec():
    v = collections.defaultdict(float)
    for _ in range(10):
        v[random.randint(0, 10)] = random.randint(0, 10) + 5
    return v


def test5d1():
    random.seed(42)
    for _ in range(10):
        v1 = randvec()
        v2 = randvec()
        ans2 = submission.sparse_vector_dot_product(v1, v2)
        if solution_exists:
            grader.require_is_equal(ans2, solution.sparse_vector_dot_product(v1, v2))


grader.add_hidden_part('5d-1-hidden', test5d1, max_points=2, description='random trials')


############################################################
# Problem 5e: increment_sparse_vector
def test5e0():
    v = collections.defaultdict(float, {'a': 5})
    submission.increment_sparse_vector(v, 2, collections.defaultdict(float, {'b': 2, 'a': 3}))
    grader.require_is_equal(collections.defaultdict(float, {'a': 11, 'b': 4}), v)


grader.add_basic_part('5e-0-basic', test5e0, max_points=1, description='simple test')


def test5e1():
    random.seed(SEED)
    for _ in range(10):
        v1 = randvec()
        v2 = randvec()
        scale = random.randint(-5, 5)

        # Run submission on a copy
        v1_sub = v1.copy()
        submission.increment_sparse_vector(v1_sub, scale, v2)

        if solution_exists:
            # Run solution on a copy
            v1_sol = v1.copy()
            solution.increment_sparse_vector(v1_sol, scale, v2)

            # Compare final sparse vectors
            grader.require_is_equal(v1_sol, v1_sub)


grader.add_hidden_part('5e-1-hidden', test5e1, max_points=2, description='random trials')


############################################################
# Problem 5f: find_most_frequent_words
def test5f0():
    grader.require_is_equal(
        {'the'},
        submission.find_most_frequent_words(
            'the quick brown fox jumps over the lazy fox the'
        )
    )
    grader.require_is_equal(
        {'a'},
        submission.find_most_frequent_words('a a b b b a a')
    )
    grader.require_is_equal(
        set(),
        submission.find_most_frequent_words('')
    )


grader.add_basic_part('5f-0-basic', test5f0, max_points=2, description='simple tests')


def test5f12(num_tokens, num_types):
    random.seed(SEED)
    text = ' '.join(str(random.randint(0, num_types)) for _ in range(num_tokens))
    out = submission.find_most_frequent_words(text)

    if solution_exists:
        grader.require_is_equal(out, solution.find_most_frequent_words(text))


grader.add_hidden_part('5f-1-hidden', lambda: test5f12(1000, 10), max_points=1, description='random trials')
grader.add_hidden_part('5f-2-hidden', lambda: test5f12(10000, 100), max_points=2, description='random trials (bigger)')


############################################################
grader.grade()