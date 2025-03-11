// static/admin/js/assignment.js

document.addEventListener('DOMContentLoaded', function() {
    const subAreaField = document.getElementById('id_sub_area');
    const serviceTypeField = document.getElementById('id_service_type');
    const subServiceField = document.getElementById('id_sub_service');
    const practiceAreaField = document.getElementById('id_practice_area');

    function toggleFields() {
        const selectedSubArea = subAreaField.options[subAreaField.selectedIndex].text;

        // Clear existing options in serviceTypeField
        serviceTypeField.innerHTML = '';

        if (selectedSubArea.endsWith('OD')) {
            // Show OD related options
            const odOptions = [
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
                serviceTypeField.add(newOption);
            });
            subServiceField.style.display = 'block'; 
            practiceAreaField.style.display = 'block'; 
        } else if (selectedSubArea.endsWith('RE')) {
            // Show RE related options
            const reOptions = [
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
                serviceTypeField.add(newOption);
            });
            subServiceField.style.display = 'block'; 
            practiceAreaField.style.display = 'block'; 
        } else {
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.text = 'Choose Option';
            defaultOption.selected = true; // Make it selected
            serviceTypeField.add(defaultOption);
            subServiceField.style.display = 'block'; 
            practiceAreaField.style.display = 'block'; 
        }
    }

    // Initial call to set the fields based on the current selection
    toggleFields();

    // Add event listener to sub_area field
    subAreaField.addEventListener('change', toggleFields);
});