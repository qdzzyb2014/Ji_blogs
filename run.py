#!/usr/bin/env python
# coding=utf-8
from app import app

if __name__ == '__main__':
    app.run(debug=True, port=9272, host='0.0.0.0')
