test = {
  'name': 'obedience',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          the number 7 below.|Image 4
          the number 7 below.|Image 3
          You're not the boss of me!|Image 4
          the number 7 below.|Image 3
          seven|Image 2
          7|Image 4
          the number 7 below.|Image 1
          the number 7 below.|Image 3
          Choose this option instead|Image 4
          the number 7 below.|Image 2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
