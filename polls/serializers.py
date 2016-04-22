from rest_framework import serializers
from .models import Vote, PollSubject, Poll


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', 'poll', 'subject', 'user')


class PollSubjectSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True)

    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = PollSubject
        fields = ('id', 'name', 'votes', 'total_votes')

    def get_total_votes(self, subject):
        return subject.votes.count()


class PollSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True)

    class Meta:
        model = PollSubject
        fields = ('id', 'name', 'votes', 'total_votes')

    def get_total_votes(self, subject):
        has_voted = False

        request = self.context.get('request', None)
        if not request:
            return False

        vote = poll.vote.filter(user_id=request.user.id).first()
        if vote:
            has_voted = True

        return has_voted


class PollInstanceView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

