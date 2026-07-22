use regex::Regex;

fn contains_ssn(input_string: &str) -> bool {
    let ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b";
    // https://docs.rs/regex/latest/regex/struct.Regex.html#method.new
    let re = Regex::new(ssn_pattern).unwrap();

    match re.find(input_string) {
        Some(_) => true,
        None => false,
    }
}

fn main() {
//    let test_input = "My Social Security number is 123-45-6789.";
    let test_input = "No number here!";

    if contains_ssn(test_input) {
        println!("Detected SSN.");
    }
    else {
        println!("No SSN detected.");
    }
}
