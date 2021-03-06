function transform(line) {
	var values = line.split(',');

	var obj = new Object();
	obj.customer_preference_id = values[0].replace(/^"/, "").replace(/"$/, "");
	obj.customer_id = values[1].replace(/^"/, "").replace(/"$/, "");
	obj.customer_preference_type = values[2].replace(/^"/, "").replace(/"$/, "");
	obj.customer_preference_value = values[3].replace(/^"/, "").replace(/"$/, "");
	obj.created_timestamp = values[4].replace(/^"/, "").replace(/"$/, "");
	obj.updated_timestamp = values[5].replace(/^"/, "").replace(/"$/, "");

	var jsonString = JSON.stringify(obj);

	return jsonString;
}