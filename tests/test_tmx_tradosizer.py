import unittest
import io

from tmxtagger import tmx_tradosizer


class TestTmxTradosizer(unittest.TestCase):

    def test_add_tree_elements_no_required_fields(self):
        """The tree should contain certain elements."""
        tmx = """<?xml version='1.0' encoding='UTF-8'?>
        <tmx version="1.4">
          <header srclang="en-US" />
          <body>
            <tu>
              <tuv xml:lang="EN-US">
                <seg>The White House</seg>
              </tuv>
              <tuv xml:lang="RU-RU">
                <seg>Белый дом</seg>
              </tuv>
            </tu>
            <tu>
              <tuv xml:lang="EN-US">
                <seg>Office of the Press Secretary</seg>
              </tuv>
              <tuv xml:lang="RU-RU">
                <seg>Офис пресс-секретаря</seg>
              </tuv>
            </tu>
          </body>
        </tmx>
        """

        tree = tmx_tradosizer.add_tree_elements(tmx, 'new_file_name')

        # Save the modified tmx file
        toF = io.BytesIO()
        tree.write(toF, encoding='UTF-8', xml_declaration=True)
        tmx_res = toF.getvalue().decode('utf-8')

        test1 = """<header srclang="en-US" creationtool="SDL Language Platform" o-tmf="SDL TM8 Format">"""
        test2 = """<prop type="x-Recognizers">RecognizeAll</prop>"""
        test3 = """<prop type="x-filename:MultipleString">"""

        self.assertIn(test1, tmx_res)
        self.assertIn(test2, tmx_res)
        self.assertIn(test3, tmx_res)

        test4 = """<prop type="x-filename:MultipleString">new_file_name</prop>"""
        self.assertIn(test4, tmx_res)

        test5 = 'new_file_name'
        self.assertIn(test5, tmx_res)

    def test_add_tree_elements_single_filename_already_exist(self):
        """Header and TUs already contains filename singleString."""
        tmx = """<?xml version="1.0" encoding="utf-8"?>
        <tmx version="1.4">
          <header creationtool="SDL Language Platform" creationtoolversion="8.1" o-tmf="SDL TM8 Format" datatype="xml" segtype="sentence" adminlang="en-US" srclang="en-US" creationdate="20231215T111805Z" creationid="alexskrn">
            <prop type="x-filename:SingleString"></prop>
            <prop type="x-TM:SingleString"></prop>
            <prop type="x-Recognizers">RecognizeAll</prop>
            <prop type="x-IncludesContextContent">True</prop>
            <prop type="x-TMName">old_file_name</prop>
            <prop type="x-TokenizerFlags">DefaultFlags</prop>
            <prop type="x-WordCountFlags">DefaultFlags</prop>
          </header>
          <body>
            <tu creationdate="20231215T112809Z" creationid="alexskrn" changedate="20240104T103646Z" changeid="alexskrn" lastusagedate="20240104T102829Z" usagecount="5">
              <prop type="x-LastUsedBy">alexskrn</prop>
              <prop type="x-Context">0, 0</prop>
              <prop type="x-Origin">TM</prop>
              <prop type="x-ConfirmationLevel">Translated</prop>
              <prop type="x-filename:SingleString">old_file_name</prop>
              <tuv xml:lang="en-US">
                <seg>2023</seg>
              </tuv>
              <tuv xml:lang="ru-RU">
                <seg>2023 год</seg>
              </tuv>
            </tu>
          </body>
        </tmx>
        """

        tree = tmx_tradosizer.add_tree_elements(tmx, 'new_file_name')

        # Save the modified tmx file
        toF = io.BytesIO()
        tree.write(toF, encoding='UTF-8', xml_declaration=True)
        tmx_res = toF.getvalue().decode('utf-8')

        test1 = """<prop type="x-filename:MultipleString">"""
        test2 = """<prop type="x-filename:SingleString"></prop>"""
        self.assertIn(test1, tmx_res)
        self.assertNotIn(test2, tmx_res)

    def test_add_tree_elements_multiple_filename_already_exist(self):
        """Header and TUs already contains filename multipleString."""
        tmx = """<?xml version="1.0" encoding="utf-8"?>
        <tmx version="1.4">
          <header creationtool="SDL Language Platform" creationtoolversion="8.1" o-tmf="SDL TM8 Format" datatype="xml" segtype="sentence" adminlang="en-US" srclang="en-US" creationdate="20231215T111805Z" creationid="alexskrn">
            <prop type="x-filename:MultipleString"></prop>
            <prop type="x-TM:SingleString"></prop>
            <prop type="x-Recognizers">RecognizeAll</prop>
            <prop type="x-IncludesContextContent">True</prop>
            <prop type="x-TMName">old_file_name</prop>
            <prop type="x-TokenizerFlags">DefaultFlags</prop>
            <prop type="x-WordCountFlags">DefaultFlags</prop>
          </header>
          <body>
            <tu creationdate="20231215T112809Z" creationid="alexskrn" changedate="20240104T103646Z" changeid="alexskrn" lastusagedate="20240104T102829Z" usagecount="5">
              <prop type="x-LastUsedBy">alexskrn</prop>
              <prop type="x-Context">0, 0</prop>
              <prop type="x-Origin">TM</prop>
              <prop type="x-ConfirmationLevel">Translated</prop>
              <prop type="x-filename:MultipleString">old_file_name</prop>
              <tuv xml:lang="en-US">
                <seg>2023</seg>
              </tuv>
              <tuv xml:lang="ru-RU">
                <seg>2023 год</seg>
              </tuv>
            </tu>
          </body>
        </tmx>
        """

        tree = tmx_tradosizer.add_tree_elements(tmx, 'new_file_name')

        # Save the modified tmx file
        toF = io.BytesIO()
        tree.write(toF, encoding='UTF-8', xml_declaration=True)
        tmx_res = toF.getvalue().decode('utf-8')

        test1 = """<prop type="x-filename:MultipleString">old_file_name</prop"""
        test2 = """ <prop type="x-filename:MultipleString">new_file_name</prop>"""
        self.assertNotIn(test1, tmx_res)
        self.assertIn(test2, tmx_res)


if __name__ == '__main__':
    unittest.main()
