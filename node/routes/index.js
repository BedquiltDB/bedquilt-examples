var express = require('express');
var router = express.Router();
var BedquiltClient = require('bedquilt').BedquiltClient;

var db = 'postgres://localhost/bedquilt_example';

/* GET home page. */

router.get('/', function(req, res) {
  BedquiltClient.connect(db, function(err, client) {
    var items = client.collection('items');
    items.find({}, function(err, result) {
      res.render('index', {
        title: 'BedquiltDB Example',
        items: result
      });
    });
  });
});

module.exports = router;
