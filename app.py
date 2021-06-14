{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# adding our dependecies\n",
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping\n",
    "\n",
    "# set up flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# add route\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "[2021-06-14 09:44:30,345] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/flask/app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/flask/app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/flask/app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/flask/_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/flask/app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/flask/app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-3-e191d5b2e6ba>\", line 3, in index\n",
      "    mars = mongo.db.mars.find_one()\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/collection.py\", line 1319, in find_one\n",
      "    for result in cursor.limit(-1):\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/cursor.py\", line 1207, in next\n",
      "    if len(self.__data) or self._refresh():\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/cursor.py\", line 1100, in _refresh\n",
      "    self.__session = self.__collection.database.client._ensure_session()\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/mongo_client.py\", line 1816, in _ensure_session\n",
      "    return self.__start_session(True, causal_consistency=False)\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/mongo_client.py\", line 1766, in __start_session\n",
      "    server_session = self._get_server_session()\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/mongo_client.py\", line 1802, in _get_server_session\n",
      "    return self._topology.get_server_session()\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/topology.py\", line 499, in get_server_session\n",
      "    None)\n",
      "  File \"/Users/AllisonChavez/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/pymongo/topology.py\", line 217, in _select_servers_loop\n",
      "    (self._error_message(selector), timeout, self.description))\n",
      "pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [Errno 61] Connection refused, Timeout: 30s, Topology Description: <TopologyDescription id: 60c76a0448bb1ddd4b9b73b7, topology_type: Single, servers: [<ServerDescription ('localhost', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('localhost:27017: [Errno 61] Connection refused')>]>\n",
      "127.0.0.1 - - [14/Jun/2021 09:44:30] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n",
      "127.0.0.1 - - [14/Jun/2021 09:44:30] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"
     ]
    }
   ],
   "source": [
    "# tells flask to run\n",
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
