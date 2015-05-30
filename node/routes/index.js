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

module.exports = router;
