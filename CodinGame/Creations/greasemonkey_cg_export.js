// ==UserScript==
// @name     CodinGame Contributions Export Button
// @include  https://www.codingame.com/contribute/view/*
// @run-at   document-idle
// @version  1
// @grant    unsafeWindow
// ==/UserScript==

add_export_button_when_ready();

function add_export_button_when_ready() {
    var subtabs = document.getElementsByClassName("cg-subtabs");
    if (subtabs.length === 0) setTimeout(add_export_button_when_ready, 500);
    else add_export_button();
}

function add_export_button() {
    var a_export = document.createElement("a");
    a_export.setAttribute("href", "#");
    a_export.setAttribute("class", "subtab");
    var a_export_text = document.createTextNode("Export...");
    a_export.appendChild(a_export_text);
    a_export.addEventListener("click", export_button_click, false);
    var subtabs = document.getElementsByClassName("cg-subtabs")[0];
    subtabs.appendChild(a_export);
}

function export_button_click() {
    var cancel_button = document.getElementsByClassName("cancel-button");
    if (cancel_button.length === 0) {
	alert('Please click on the "EDIT" button first.');
	return false;
    }
    
    var contrib = [];
    function contrib_push(field, content) {
	contrib.push("===== BEGIN " + field + " =====\n");
	contrib.push(content);
	contrib.push("\n=====  END  " + field + " =====\n\n\n");
    }
    
    var title = document.getElementsByName("title")[0].value;
    contrib_push("Title", title);
    var statement = document.getElementsByName("statement")[0].value;
    contrib_push("Statement", statement);
    var inputDescription = document.getElementsByName("inputDescription")[0].value;
    contrib_push("Input Description", inputDescription);
    var outputDescription = document.getElementsByName("outputDescription")[0].value;
    contrib_push("Output Description", outputDescription);
    var constraints = document.getElementsByName("constraints")[0].value;
    contrib_push("Constraints", constraints);
    
    for (let i=0; ; ++i) {
	let input_test = document.getElementsByName("input_test" + i);
	if (input_test.length === 0) break;
	input_test = input_test[0].value;
	contrib_push("Input Test " + i, input_test);
	let output_test = document.getElementsByName("output_test" + i)[0].value;
	contrib_push("Output Test " + i, output_test);
	let input_validator = document.getElementsByName("input_validator" + i)[0].value;
	contrib_push("Input Validator " + i, input_validator);
	let output_validator = document.getElementsByName("output_validator" + i)[0].value;
	contrib_push("Output Validator " + i, output_validator);
    }
    
    var solutionLanguage = document.getElementsByName("solutionLanguage")[0].value;
    contrib_push("Solution Language", solutionLanguage);
    // monaco editor https://github.com/Microsoft/monaco-editor/issues/37
    var monaco = unsafeWindow.monaco.editor.getModels();
    var solution = monaco[0].getValue();
    contrib_push("Solution", solution);
    var stub = monaco[1].getValue();
    contrib_push("Stub", stub);
    
    var blob = new Blob(contrib);
    var blob_url = window.URL.createObjectURL(blob);

    var virtual_a = document.createElement("a");
    virtual_a.setAttribute("href", blob_url);
    virtual_a.setAttribute("download", "contribution.txt");
    return virtual_a.click();
}
