import web

urls = (
    '/(.*)', 'index'
)
render = web.template.render("resources/")
app = web.application(urls, globals())

class hello:
    def GET(self, name, age):
        #we are looking at resources folder and looking for main.html file's parameters
        return render.main(name, age)

if __name__ == "__main__":
    app.run()