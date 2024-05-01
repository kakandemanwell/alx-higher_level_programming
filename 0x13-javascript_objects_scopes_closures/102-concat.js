#!/usr/bin/node

const fs = require('fs');

const SourceFile1 = process.argv[2];
const SourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const content1 = fs.readFileSync(SourceFile1, 'utf8');

const content2 = fs.readFileSync(SourceFile2, 'utf8');

// const combinedContent = content1 + content2;
const combinedContent = `${content1}\n${content2}`
fs.writeFileSync(destinationFile, combinedContent, 'utf-8');