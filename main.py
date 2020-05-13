from src.transform import Transform

class ParseXML():
  '''
  Class ParseXML
  '''

  @classmethod
  def transform(self, template, xml):
    data = Transform.transform(template, xml)
    print(data)
    


ParseXML.transform("sssss", "")