from parser_class import Parser

parser = Parser('https://www.kivano.kg/noutbuki', 'news.txt')
user_agent = 'User-AgentMozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
parser.run()
print(parser.results)
print(parser.get_html())