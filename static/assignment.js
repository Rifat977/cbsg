// static/admin/js/assignment.js

document.addEventListener('DOMContentLoaded', function() {
    // const subAreaField = document.getElementById('id_sub_area');
    const serviceTypeField = document.getElementById('id_service_type');
    const subServiceField = document.getElementById('id_sub_service');

    function toggleFields() {
        // const selectedSubArea = subAreaField.options[subAreaField.selectedIndex].text;
        const selectedserviceType = serviceTypeField.options[serviceTypeField.selectedIndex].text;

        // Clear existing options in serviceTypeField
        subServiceField.innerHTML = '';

        if (selectedserviceType.includes('Organization Development')) {
            // Show OD related options
            const odOptions = [
                { value: "", text: "Choose Option" },
                { value: 'Organizational Capacity Assesment', text: 'Organizational Capacity Assesment' },
                { value: 'Change Management', text: 'Change Management' },
                { value: 'Training & Facilitation', text: 'Training & Facilitation' },
                { value: 'Project Cycle Management', text: 'Project Cycle Management' },
                { value: 'ICT/MIS Development', text: 'ICT/MIS Development' }
            ];
            odOptions.forEach(option => {
                const newOption = document.createElement('option');
                newOption.value = option.value;
                newOption.text = option.text;
                subServiceField.add(newOption);
            });
            // subServiceField.style.display = 'block'; 
        } else if (selectedserviceType.includes('Research & Evaluation')) {
            // Show RE related options
            const reOptions = [
                { value: "", text: "Choose Option" },
                { value: 'Baseline & Program Evaluation', text: 'Baseline & Program Evaluation' },
                { value: 'Project Program Evaluation', text: 'Project Program Evaluation' },
                { value: 'Market Survey', text: 'Market Survey' },
                { value: 'Thematic Research', text: 'Thematic Research' },
                { value: 'Impact Assesment', text: 'Impact Assesment' },
                { value: 'Performance Studies', text: 'Performance Studies' },
                { value: 'Preception Studies', text: 'Preception Studies' },
            ];
            reOptions.forEach(option => {
                const newOption = document.createElement('option');
                newOption.value = option.value;
                newOption.text = option.text;
                subServiceField.add(newOption);
            });
            // subServiceField.style.display = 'block'; 
        } else {
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.text = 'Choose Option';
            defaultOption.selected = true; // Make it selected
            subServiceField.add(defaultOption);
            // subServiceField.style.display = 'block'; 
        }
    }

    // Initial call to set the fields based on the current selection
    toggleFields();

    // Add event listener to sub_area field
    serviceTypeField.addEventListener('change', toggleFields);
});