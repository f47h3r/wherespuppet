# -*- coding: utf-8 -*-
db = DAL("sqlite://storage.db")

db.define_table('image',
    Field('file', 'upload', requires=IS_NOT_EMPTY()),
    Field('thumb','upload',writable=False,readable=False),
    Field('title', requires=IS_NOT_EMPTY()),
    Field('handle', requires=IS_NOT_EMPTY()),
    Field('location', requires=IS_NOT_EMPTY()),
    Field('latitude', requires=IS_NOT_EMPTY(), readable=False, writable=False),
    Field('longitude', requires=IS_NOT_EMPTY(), readable=False, writable=False),
    Field('pub_date','datetime', readable=False, writable=False, default=request.now))
    
db.define_table('comment',
    Field('image_id', db.image),
    Field('author'),
    Field('email'),
    Field('body', 'text'))

db.comment.image_id.writable = db.comment.image_id.readable = False
db.comment.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.comment.author.requires = IS_NOT_EMPTY()
db.comment.email.requires = IS_EMAIL()
db.comment.body.requires = IS_NOT_EMPTY()
db.image.file.requires = IS_IMAGE()
