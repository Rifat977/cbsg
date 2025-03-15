// static/admin/js/assignment.js

document.addEventListener('DOMContentLoaded', function() {
    // const subAreaField = document.getElementById('id_sub_area');
    const serviceTypeField = document.getElementById('id_service_type');
    const subServiceField = document.getElementById('id_sub_service_area');

    const originalOptions = Array.from(subServiceField.options).map(option => ({
        value: option.value,
        text: option.text
    }));

    // Classify options into storedOdOptions and storedReOptions
    const storedOdOptions = originalOptions.filter(option => option.text.endsWith('OD'));
    const storedReOptions = originalOptions.filter(option => option.text.endsWith('RE'));


    function toggleFields() {

        
        // const selectedSubArea = subAreaField.options[subAreaField.selectedIndex].text;
        const selectedserviceType = serviceTypeField.options[serviceTypeField.selectedIndex].text;


        // Clear existing options
        subServiceField.innerHTML = '';


        if (selectedserviceType.includes('Organization Development')) {
            
            // Add only options that do not end with 'RE' and avoid duplicates
            originalOptions.forEach(option => {
                if (!option.text.endsWith('RE') && !Array.from(subServiceField.options).some(existingOption => existingOption.value === option.value)) {
                    const newOption = document.createElement('option');
                    newOption.value = option.value;
                    newOption.text = option.text;
                    subServiceField.add(newOption);
                }
            });

            storedOdOptions.forEach(option => {
                // Avoid adding duplicates from storedOdOptions
                if (!Array.from(subServiceField.options).some(existingOption => existingOption.value === option.value)) {
                    const newOption = document.createElement('option');
                    newOption.value = option.value;
                    newOption.text = option.text;
                    subServiceField.add(newOption);
                }
            });


        } else if (selectedserviceType.includes('Research & Evaluation')) {
            // Add only options that do not end with 'OD' and avoid duplicates
            originalOptions.forEach(option => {
                if (!option.text.endsWith('OD') && !Array.from(subServiceField.options).some(existingOption => existingOption.value === option.value)) {
                    const newOption = document.createElement('option');
                    newOption.value = option.value;
                    newOption.text = option.text;
                    subServiceField.add(newOption);
                }
            });

            storedReOptions.forEach(option => {
                // Avoid adding duplicates from storedReOptions
                if (!Array.from(subServiceField.options).some(existingOption => existingOption.value === option.value)) {
                    const newOption = document.createElement('option');
                    newOption.value = option.value;
                    newOption.text = option.text;
                    subServiceField.add(newOption);
                }
            });
        }
    }

    // Initial call to set the fields based on the current selection
    toggleFields();

    // Add event listener to sub_area field
    serviceTypeField.addEventListener('change', toggleFields);
});