function beautify {
  PATH=$(npm bin):$PATH
  mkdir -p alfredtmp && cd alfredtmp
  pbpaste > tmp.js
  js-beautify tmp.js > tmp.coffee
  cat tmp.coffee | pbcopy
  cd ../ && rm -r alfredtmp
}

if [ -d "node_modules" ]; then
  beautify
else
  npm install js-beautify
  beautify
fi