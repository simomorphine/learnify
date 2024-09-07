from flask import render_template, redirect, url_for, request, flash
from . import evaluations
from .forms import EvaluationForm

@evaluations.route('/create', methods=['GET', 'POST'])
def create_evaluation():
    form = EvaluationForm()
    if form.validate_on_submit():
        # Handle file uploads
        uploaded_files = request.files.getlist('file_uploads')
        additional_files = request.files.getlist('additional_files')

        # Save files, handle form data, etc.
        # For example, save uploaded_files and additional_files to a directory or database
        
        flash('Evaluation created successfully!', 'success')
        return redirect(url_for('evaluations.create_evaluation'))

    return render_template('create_evaluation.html', form=form)
