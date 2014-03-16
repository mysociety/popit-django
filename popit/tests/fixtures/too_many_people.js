// See https://github.com/powmedia/pow-mongodb-fixtures for the format used in
// this file

exports.persons = (function() {
    var i, result = {};
    for (i = 0; i < 65; ++i) {
        result[i] = {
            _id: "generated-person-" + i,
            name: "Generated Person " + i

        };
    }
    return result;
}());
