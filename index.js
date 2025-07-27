// functions/index.js
const { exec } = require('child_process');
const functions = require('firebase-functions');
const fs = require('fs');

exports.extractPdfHeadings = functions.https.onRequest((req, res) => {
  const file = req.body.pdfBase64;
  fs.writeFileSync('/tmp/input.pdf', Buffer.from(file, 'base64'));

  exec('python3 extract_outline.py /tmp/input.pdf', (error, stdout, stderr) => {
    if (error) {
      console.error(stderr);
      return res.status(500).send('Error');
    }
    res.send(stdout);
  });
});
