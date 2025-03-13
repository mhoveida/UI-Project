// Maddison Hoveida UNI: mh4572
$(document).ready(function() {
    loadPopularBungalows();

    $(document).on("submit", "#search-form", function(e) {
        var searchInput = $("#search-input").val().trim();
        
        if (!searchInput) {
            e.preventDefault();
            $("#search-input").val("").focus();
        }
    });

    // Add form submission with validation
    $("#add-form").on("submit", function(e) {
        e.preventDefault();
        
        // Form validation
        const form = $(this)[0];
        if (form.checkValidity() === false) {
            e.stopPropagation();
            $(this).addClass('was-validated');
            return;
        }
        
        // Prepare data
        const newBungalow = {
            title: $("#title").val(),
            image: $("#image").val(),
            year: $("#year").val(),
            summary: $("#summary").val(),
            price_per_night: $("#price_per_night").val(),
            location: $("#location").val(),
            amenities: $("#amenities").val().split(",").map(item => item.trim()),
            rating: $("#rating").val(),
            similar_bungalow_ids: $("#similar_bungalow_ids").val().split(",").map(item => item.trim()),
            activities: $("#activities").val().split(",").map(item => item.trim()),
            best_season: $("#best_season").val().split(",").map(item => item.trim()),
            reviews: []
        };
        
        // Submit data via AJAX
        $.ajax({
            url: "/add",
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(newBungalow),
            success: function(data) {
                // Show success message
                $("#success-message").show();
                $("#view-link").attr("href", "/view/" + data.id);
                
                // Reset form
                $("#add-form").removeClass('was-validated');
                $("#add-form")[0].reset();
                $("#title").focus();
            },
            error: function(xhr, status, error) {
                alert("Error: " + (xhr.responseJSON ? xhr.responseJSON.error : "Unknown error"));
            }
        });
    });

    // Edit form submission
    $("#edit-form").on("submit", function(e) {
        e.preventDefault();
        
        // Form validation
        const form = $(this)[0];
        if (form.checkValidity() === false) {
            e.stopPropagation();
            $(this).addClass('was-validated');
            return;
        }
        
        const bungalowId = $(this).data("id");
        const updatedBungalow = {
            title: $("#title").val(),
            image: $("#image").val(),
            year: $("#year").val(),
            summary: $("#summary").val(),
            price_per_night: $("#price_per_night").val(),
            location: $("#location").val(),
            amenities: $("#amenities").val().split(",").map(item => item.trim()),
            rating: $("#rating").val(),
            similar_bungalow_ids: $("#similar_bungalow_ids").val().split(",").map(item => item.trim()),
            activities: $("#activities").val().split(",").map(item => item.trim()),
            best_season: $("#best_season").val().split(",").map(item => item.trim())
            // reviews will be preserved in the server
        };

        $.ajax({
            url: "/edit/" + bungalowId,
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(updatedBungalow),
            success: function(response) {
                window.location.href = "/view/" + bungalowId;
            },
            error: function(xhr, status, error) {
                alert("Error: " + (xhr.responseJSON ? xhr.responseJSON.error : "Unknown error"));
            }
        });
    });

    // Handle discard changes button
    $("#discard-btn").on("click", function() {
        $('#confirmModal').modal('show');
    });

    // Handle confirm discard
    $("#confirm-discard").on("click", function() {
        const bungalowId = $("#edit-form").data("id");
        window.location.href = "/view/" + bungalowId;
    });
    
    // Add Review Button
    $("#add-review-btn").on("click", function() {
        $("#reviewModal").modal("show");
    });

    // Submit Review
    $("#submit-review").on("click", function() {
        const form = $("#review-form")[0];
        if (form.checkValidity() === false) {
            $("#review-form").addClass('was-validated');
            return;
        }
        
        const bungalowId = $("#review-form").data("bungalow-id");
        const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        const now = new Date();
        const formattedDate = months[now.getMonth()] + " " + now.getFullYear();
        
        const reviewData = {
            reviewer_name: $("#reviewer-name").val(),
            rating: $("#review-rating").val(),
            date: formattedDate,
            text: $("#review-text").val()
        };
        
        $.ajax({
            url: "/add_review/" + bungalowId,
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(reviewData),
            success: function(response) {
                // Close modal and reload page to show new review
                $("#reviewModal").modal("hide");
                location.reload();
            },
            error: function(xhr, status, error) {
                alert("Error: " + (xhr.responseJSON ? xhr.responseJSON.error : "Unknown error"));
            }
        });
    });
});

function loadPopularBungalows() {
    $.ajax({
        url: "/api/popular_bungalows",
        method: "GET",
        dataType: "json",
        success: function(data) {
            $("#popular-bungalows").empty();

            if (data && data.length > 0) {
                $.each(data, function(index, bungalow) {
                    var card = `
                        <div class="col-md-4 mb-4">
                            <div class="card bungalow-card h-100">
                                <a href="/view/${bungalow.id}">
                                    <img src="${bungalow.image}" class="card-img-top" alt="View of ${bungalow.title} overwater bungalow">
                                </a>
                                <div class="card-body">
                                    <h5 class="card-title">${bungalow.title}</h5>
                                    <p class="card-text">
                                        <i class="fas fa-map-marker-alt text-danger me-1"></i> ${bungalow.location} 
                                        <span class="mx-2">|</span> 
                                        <i class="fas fa-star text-warning"></i> ${bungalow.rating}/5.0
                                    </p>
                                    <p class="card-text text-primary fw-bold">${bungalow.price_per_night} per night</p>
                                    <a href="/view/${bungalow.id}" class="btn btn-primary">View Details</a>
                                </div>
                            </div>
                        </div>
                    `;
                    $("#popular-bungalows").append(card);
                });
            } else {
                $("#popular-bungalows").html("<div class='col-12'><p>No popular bungalows found</p></div>");
            }
        },
        error: function(xhr, status, error) {
            console.error("Error loading popular bungalows:", error);
            $("#popular-bungalows").html("<div class='col-12'><p>Error loading popular bungalows</p></div>");
        }
    });
}