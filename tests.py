from llt.utils import get_key_by_value

SAMPLE = (
    ('a', 'apple'),
    ('b', 'boy'),
)

if __name__ == '__main__':

    assert get_key_by_value(SAMPLE, 'apple') == 'a'
    assert get_key_by_value(SAMPLE, 'boy') == 'b'
