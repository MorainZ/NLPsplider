import pdfcrowd

# create an API client instance
client = pdfcrowd.Client("morningrain", "12ab704789a57360d41232b313ed80ed")

# # convert a web page and store the generated PDF into a pdf variable
# pdf = client.convertURI('http://www.google.com')
#
# # convert an HTML string and save the result to a file
# output_file = open('html.pdf', 'wb')
# html="<head></head><body>My HTML Layout</body>"
# client.convertHtml(html, output_file)
# output_file.close()

# convert an HTML file
output_file = open('scikit-learn文本挖掘系列 17-主题抽取.pdf', 'wb')
client.convertFile('scikit-learn文本挖掘系列 17-主题抽取.html', output_file)
output_file.close()


