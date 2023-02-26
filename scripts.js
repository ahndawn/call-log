const communitySelect = document.querySelector('#community-select');
const areaSelect = document.querySelector('#area-select');
    
communitySelect.addEventListener('change', (event) => {
    const community = event.target.value;
    if (community === 'hunters_run') {
        areaSelect.value = 'north';
    } else if (community === 'valencia_cove') {
        areaSelect.value = 'central';
    } else if (community === 'ibis') {
        areaSelect.value = 'west';
    }
});