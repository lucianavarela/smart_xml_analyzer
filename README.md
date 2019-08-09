# smart-xml-analyzer
This repository contains implementation of simple XML-analyzer that can find one specified element in different documents. 

## Details
The algorithm is implemented using simple `Criteria` concept: an object that can find elements of HTML-document based on some criteria e.g. `class` attribute value.

How it works: multiple criterias are applied to the document to find groups of objects, then we find such object that is contained in maximum number of groups or, as it was implemented, has highest score in all groups. With high probability it'll be target button.

Score is calculated between 0 to 1 as coefficient that represents largest common substring length between attribute values. For example, if source button has `class='btn btn-success'` and two target buttons have accordingly `class='btn-success btn-check'` and `class='btn btn-danger'`, the first one will have better score because of `btn-success` substring.

## Using
```bash
git clone https://github.com/JoshuaLight/smart-xml-analyzer
cd smart-xml-analyzer/bin
./main [origin] [target] [element_id]
```
