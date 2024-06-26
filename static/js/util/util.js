class Util {
    constructor()
    {
        document.addEventListener("DOMContentLoaded", function () {
            UTIL.import(`${STATICS}js/util/validate.js`).then(validate => { window.VALIDATE = new validate.default(); });
            UTIL.initWidgets();
        });
    }

    async import(js, version=1)
    {
        return await import(js + "?v=" + version);
    }

    initWidgets()
    {
        this.import(`${STATICS}js/util/widget/AutoComplete.js`, 4).then(autoComplete => {
            this.AutoComplete = autoComplete.default;
            this.initAutoComplete();
        });
        this.import(`${STATICS}js/util/widget/AutoComplete2.js`, 4).then(autoComplete => {
            this.AutoComplete2 = autoComplete.default;
            this.initAutoComplete2();
        });
        this.import(`${STATICS}js/util/widget/GridJS.js`, 3).then(gridJS => {
            this.GridJS = gridJS.default;
        });
        this.import(`${STATICS}js/util/widget/DataTable.js`, 7).then(dataTable => {
            this.DataTable = dataTable.default;
        });
        this.import(`${STATICS}js/util/widget/DateRangePicker.js`, 1).then(dateRangePicker => {
            this.DateRangePicker = dateRangePicker.default;
        });
        this.import(`${STATICS}js/util/widget/DatePicker.js`, 1).then(datePicker => {
            this.DatePicker = datePicker.default;
        });
        this.import(`${STATICS}js/util/widget/Slider.js`, 4).then(slider => {
            this.Slider = slider.default;
            this.initSlider();
        });
        this.import(`${STATICS}js/util/widget/Toast.js`, 2).then(toast => {
            this.Toast = toast.default;
        })
        this.import(`${STATICS}js/util/widget/FileUploader.js`, 1).then(fileUploader => {
            this.FileUploader = fileUploader.default;
        })
        this.import(`${STATICS}js/util/widget/Steps.js`, 1).then(steps => {
            this.Steps = steps.default;
        });
        setTimeout(this.handleEvents, 100);
    }

    initAutoComplete()
    {
        let autoCompleteElements = document.getElementsByClassName("auto-complete");
        for (let i=0; i < autoCompleteElements.length; i++) {
            new this.AutoComplete(autoCompleteElements[i].getAttribute("id"));
        }
    }

    initAutoComplete2()
    {
        let autoCompleteElements = document.getElementsByClassName("auto-complete-2");
        for (let i=0; i < autoCompleteElements.length; i++) {
            new this.AutoComplete2(autoCompleteElements[i]);
        }
    }

    initSlider() {
        let sliderElements = document.getElementsByClassName("slider");
        for (let i=0; i < sliderElements.length; i++) {
            new this.Slider(sliderElements[i].getAttribute("id"));
        }
    }

    handleEvents()
    {
        document.addEventListener('click', function(event) {
            if (!event.target.matches('.auto-complete-input')) {
                let ulElements = document.getElementsByClassName("auto-complete-menu");

                for (let i=0; i < ulElements.length; i++) {
                    ulElements[i].style.display = "none";
                }
            }
        });
    }

    header(to)
    {
        if (!to.startsWith('https://') && !to.startsWith('http://')) {
            window.location.assign(ROOTPATH + to);
        } else {
            window.location.assign(to);
        }
    }

    formJson(data)
    {
        let jsonData = {};
        for (let [key, value] of data.entries()) {
            jsonData[key] = value;
        }
        return jsonData
    }

    empty(value)
    {
        return typeof value === "undefined" || value === null || value.trim() === "";
    }
}

window.UTIL = new Util();
