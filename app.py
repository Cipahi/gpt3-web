import web
import summarizer

urls = (
    '/(.*)', 'demo'
)
app = web.application(urls, globals())

class demo:
    def GET(self, file):
        if not file:
            file = 'input.txt'
        result = summarizer.analyse(file)
        return result

if __name__ == "__main__":
    app.run()