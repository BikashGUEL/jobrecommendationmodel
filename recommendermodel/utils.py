from django.core.exceptions import ObjectDoesNotExist
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from .models import Student, Job

def model_implementation(student_id):
    try:
        student_info = Student.objects.get(student_id=student_id)
        student_tags = [student_info.student_tags]

        tfidf = TfidfVectorizer(stop_words='english')
        job_vector = tfidf.fit_transform(Job.objects.values_list('job_tags', flat=True))
        student_vector = tfidf.transform(student_tags)

        cosine_similarity_score = cosine_similarity(student_vector, job_vector)

        top_indices = cosine_similarity_score[0].argsort()[-5:][::-1]
        top_scores = cosine_similarity_score[0][top_indices]

        sentiment_scores = [TextBlob(desc).sentiment.polarity for desc in Job.objects.values_list('job_tags', flat=True)]

        weighted_score = cosine_similarity_score[0] * sentiment_scores

        top_indices_with_sentiment = weighted_score.argsort()[-5:][::-1]
        top_scores_with_sentiment = weighted_score[top_indices_with_sentiment]
        print("Top job with sentiment",top_indices_with_sentiment)
        all_job_titles = Job.objects.values_list('job_title', flat=True)
        top_job_titles = [all_job_titles[int(i)] for i in top_indices_with_sentiment]
        print("Recommendatiion Top List", top_job_titles)
       
        return top_job_titles
    except ObjectDoesNotExist:
        print(f"No Student object exists with student_id {student_id}")