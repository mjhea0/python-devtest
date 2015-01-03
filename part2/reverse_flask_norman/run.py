from project.app import app
import os

#port = int(os.environ.get('PORT', 5000))
#app.run(host='0.0.0.0', port=port)

# if pushing to heroku, use the two lines above

if __name__=="__main__":
    app.run(debug=True)

