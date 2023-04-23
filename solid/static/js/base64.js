var getBase64 = function getBase64(file, callback) {
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {
        var data = reader.result;
        var res = data.split(",");
        callback(res[1]);
    };
    reader.onerror = function (error) {
        console.log('Error: ', error);
        callback("");
    };
}