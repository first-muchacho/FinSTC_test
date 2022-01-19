import lxml.etree as ET


dom = ET.parse("test.xml")
xslt = ET.parse("change.xslt")
transform = ET.XSLT(xslt)
newdom = transform(dom)
newfile = str(newdom)

with open("result.xml", 'w') as f:
    f.write(newfile)
