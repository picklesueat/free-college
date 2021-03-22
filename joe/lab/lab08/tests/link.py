test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab09 import *
          >>> link = Link(1000)
          >>> link.first
          1000
          >>> link.rest is Link.empty
          True
          >>> link = Link(1000, 2000)
          Error
          >>> link = Link(1000, Link())
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab09 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          1
          >>> link.rest.first
          2
          >>> link.rest.rest.rest is Link.empty
          True
          >>> link.first = 9001
          >>> link.first
          9001
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          3
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link2.rest.first
          9338923f09aac77121029c604f7ce4f3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from lab09 import *
          >>> link = Link(5, Link(6, Link(7)))
          >>> link                  # Look at the __repr__ method of Link
          c4be84510df152813dfac1955471823d
          # locked
          >>> print(link)          # Look at the __str__ method of Link
          9e4aa8611562bf27deef2ea24cf05283
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
