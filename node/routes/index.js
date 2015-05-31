var express = require('express');
var router = express.Router();
var BedquiltClient = require('bedquilt').BedquiltClient;

var db = 'postgres://localhost/bedquilt_example';

/* GET home page. */
router.get('/', function(req, res) {
  BedquiltClient.connect(db, function(err, client) {
    var notes = client.collection('notes');
    notes.find({}, function(err, result) {
      res.render('index', {
        title: 'BedquiltDB Example',
        notes: result
      });
    });
  });
});

/* Create a new note */
router.post('/note', function(req, res) {
  var data = req.body;
  BedquiltClient.connect(db, function(err, client) {
    var notes = client.collection('notes');
    var doc = {
      title: data.title,
      description: data.description,
      tags: []
    };
    notes.save(doc, function(err, result) {
      res.redirect('/');
    });
  });
});

/* Delete a note */
router.post('/note/:id/delete', function(req, res) {
  var noteId = req.params.id;
  BedquiltClient.connect(db, function(err, client) {
    var notes = client.collection('notes');
    notes.removeOneById(noteId, function(err, result) {
      res.redirect('/');
    });
  });
});

module.exports = router;
